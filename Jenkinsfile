pipeline {
  agent {
    docker {
      image 'cpp_base:1.0.0'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  environment {
    CONAN_HOME = "${WORKSPACE}/.conan_cache"
  }

  stages {
    stage('Initialize') {
      steps {
        sh 'conan profile detect --force'
      }
    }

    stage('Build Libs') {
      steps {
        script {
          // We build and export to local conan cache inside the container
          sh 'conan create libcore/ --build=missing'
          sh 'conan create libutils/ --build=missing'
          sh 'conan create libmarket/ --build=missing'
        }
      }
    }

    stage('Build Executables') {
      steps {
	dir('gateway') {
	  sh 'conan install . --build=missing'
          sh 'cmake --preset conan-release'
          sh 'cmake --build --preset conan-release'
	}
	dir('engine') {
          sh 'conan install . --build=missing'
          sh 'cmake --preset conan-release'
          sh 'cmake --build --preset conan-release'
	}
      }
    }

    stage('Create Portable Bundle') {
      steps {
        script {
          sh 'mkdir -p product_bundle'
          sh 'cp gateway/build/Release/gateway product_bundle/'
          sh 'cp engine/build/Release/engine product_bundle/'
          sh 'find ${CONAN_HOME}/p -name "*.so" -exec cp {} product_bundle/ \\;'
          sh '''
            echo "#!/bin/sh" > product_bundle/run_engine.sh
            echo "export LD_LIBRARY_PATH=\\$(dirname \\\$0)" >> product_bundle/run_engine.sh
            echo "./engine" >> product_bundle/run_engine.sh
            chmod +x product_bundle/run_engine.sh
          '''
         sh '''
            echo "#!/bin/sh" > product_bundle/run_gateway.sh
            echo "export LD_LIBRARY_PATH=\\$(dirname \\\$0)" >> product_bundle/run_gateway.sh
            echo "./gateway" >> product_bundle/run_gateway.sh
            chmod +x product_bundle/run_gateway.sh
          '''
          sh 'tar -cvzf LegacyProject_Product_v1.0.tar.gz product_bundle/'
        }
      }
    }

    stage('Archive Artifacts') {
      steps {
        archiveArtifacts artifacts: 'LegacyProject_Product_v1.0.tar.gz'
      }
    }
  }
}
