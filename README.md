DLXassembler
============

A python assembler for the DLX instruction set.

**Requirements:**  
* ply==3.4

## Running Assembler.py 
Below you'll find instructions on how to run Assembler.py on different systems.

### VirtualBox + Vagrant + Chef + Librarian-Chef + VirtualEnv (the cool way)
Within this project you will find a Vagrantfile and Cheffile. These two files together along with the right software can
 be used to automatically generate a virtual machine. This virtual machine is configured to run Assembler.py.  

1. Install [VirtualBox](https://www.virtualbox.org/).  
2. Install [Vagrant](https://www.vagrantup.com/).  
3. Install Librarian Chef.  
    (For Windows)  
    ```$ vagrant plugin install vagrant-librarian-chef-nochef```  
      
    (For Linux)  
    ```$ vagrant plugin install vagrant-librarian-chef```    
4. Run ```vagrant up``` from within the DLXassembler directory.
5. Activate the python3 virtualenv.
    ```$ source ~/.virtualenvs/DLXassembler/bin/activate```
6. Move into the /vagrant/ directory.
    ```$ cd /vagrant/```
7. Run ```./run.pl``` or call Assembler.py directly by running ```python Assembler.py <input_file_name>```.

### Student Machine (ewwwww)
You'll need to use install the appropriate packages using pip3 and the included requirements.txt file.  

1. Install required packages.  

    ```$ pip3 install < requirements.txt```  
    
2. Run ```./run.pl``` or call Assembler.py directly by running ```python3 Assembler.py <input_file_name>```.