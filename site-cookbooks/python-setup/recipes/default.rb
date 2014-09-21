#
# Cookbook Name:: python-setup
# Recipe:: default
#
# Copyright 2014, Nathan Hernandez
#
# All rights reserved - Do Not Redistribute
#

include_recipe "python"

directory '/home/vagrant/.virtualenvs' do
    owner 'vagrant'
    group 'vagrant'
    action :create
end

python_virtualenv '/home/vagrant/.virtualenvs/DLXassembler' do
   interpreter "python3"
   owner 'vagrant'
   group 'vagrant'
   action :create
end

python_pip "ply" do
  virtualenv "/home/vagrant/.virtualenvs/DLXassembler"
end