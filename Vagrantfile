Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.04"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.synced_folder "./tmp/mydata", "/home/vagrant/mydata"
  config.vm.synced_folder "./app", "/home/vagrant/app"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y curl git python3 python3-pip docker.io
    usermod -aG docker vagrant
    curl -sfL https://get.k3s.io | sh -
  SHELL
end
