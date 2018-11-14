# Creates a Postgres container for us to use during development
docker_image = ENV['DOCKER_IMAGE'] ? ENV['DOCKER_IMAGE'] : 'postgres:latest'
postgres_user = ENV['POSTGRES_USER'] ? ENV['POSTGRES_USER'] : 'django'
postgres_password = ENV['POSTGRES_PASSWORD'] ? ENV['POSTGRES_PASSWORD'] : 'PokerScores123'
postgres_db = ENV['POSTGRES_DB'] ? ENV['POSTGRES_DB'] : 'pokerscores'

Vagrant.configure('2') do |config|
  config.vm.provider 'docker' do |d|
    # pull container from registry
    d.image = docker_image
    # tell the container to stay running, even when /bin/bash exits (default command)
    d.create_args = ['-t']
    # connect localhost only Postgres port to the container's Postgres port
    d.ports = ["127.0.0.1:5432:5432"]
    # send environment variables so Postgres can set a password
    d.env = {
      'POSTGRES_USER' => postgres_user,
      'POSTGRES_PASSWORD' => postgres_password,
      'POSTGRES_DB' => postgres_db,
    }
  end

  config.vm.provision 'docker' do |d|
    d.run 'default'
  end
end
