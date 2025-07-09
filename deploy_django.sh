function set_python_venv() {
     
    environment_name="venv"
    echo "creating venv: python -m venv $environment_name"
    python -m venv $environment_name
    
    echo "activating the venv" 
    source $environment_name/Scripts/activate

    echo "upgrading pip: python -m pip install --upgrade pip"
    python -m pip install --upgrade pip

}

function setup_django() {
    echo "installing django: pip3 install django"
    pip install django

    # Create main project folder
    python -m django startproject src .

    cd $project_name
    echo "to run project: python manage.py runserver"

    echo "*use underscore for doing spaces in name"
    read -p "Tell me your project name: " project_name

    # Create application folder
    python manage.py startapp $project_name
}


echo "Setting up python_venv:"
set_python_venv

echo "setup_django Project"
setup_django