#
# Cookbook Name:: python-setup
# Recipe:: default
#
# Copyright 2014, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

include_recipe "python"

directory '/environments' do
    owner 'vagrant'
    group 'vagrant'
    action :create
end

python_virtualenv '/environments/DLXassembler' do
   interpreter "python3"
   owner 'vagrant'
   group 'vagrant'
   action :create
end