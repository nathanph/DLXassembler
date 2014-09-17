#
# Cookbook Name:: python-setup
# Recipe:: default
#
# Copyright 2014, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

include_recipe "python"

python_virtualenv '/vagrant/environment' do
   interpreter "python3"
   owner 'vagrant'
   group 'vagrant'
   action :create
end