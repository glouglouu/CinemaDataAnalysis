$pythonOs = (python ./checkOS.py).Trim()

if ($pythonOs -eq "Windows") {
    Write-Host "This script is for Linux/macOS. Use .\setup.ps1 for Windows."

}
else {
    Write-Host "Linux/macOS system detected. Running Linux/macOS commands..."

    # Step 1: Create a virtual environment
    python3 -m venv env

    # Step 2: Activate the virtual environment
    source env/bin/activate

    # Step 3: Install dependencies
    pip3 install -r requirements.txt

    # Step : Capture the state of dependencies in requirements.txt
    pip3 freeze > requirements.txt
}

