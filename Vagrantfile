VAGRANT_EXPERIMENTAL = 1
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  #config.vm.box = "fedora/33-cloud-base"

  config.vm.disk :disk, size: "80GB", name: "varlib_containers"  

  config.vm.box_check_update = true

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 443, host: 8443


  config.vm.provider "virtualbox" do |vb|
    vb.cpus = "8"
    vb.memory = "16384"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end

  if Vagrant.has_plugin?("vagrant-vb-guest")
      config.vbguest.auto_update = true
      config.vbguest.no_remote = true
  end
end
