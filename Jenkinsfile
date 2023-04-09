pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                sh 'echo "Building Containers"'
                sh 'docker-compose -f docker-compose.prod.yml build'
                sh 'docker-compose -f docker-compose.prod.yml up -d'
            }
        }
        stage('Test'){
            steps {
                sh 'echo "Testing web Container"'
                sh 'docker exec -T web python ieee/manage.py test ./ieee'
            }
        }
        stage('Deploy') { 
            steps { 
                sh 'echo "Deploying to staging"'
                sh 'docker-compose -f docker-compose.prod.yml exec -T web python manage.py migrate'
                sh 'docker-compose -f docker-compose.prod.yml exec -T web python manage.py makemigrations events'
                sh 'docker-compose -f docker-compose.prod.yml exec -T web python manage.py migrate events'
            }
        }
    }
}