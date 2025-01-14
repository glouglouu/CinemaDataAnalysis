$pythonOs = (python ./checkOS.py).Trim()

if ($pythonOs -eq "Windows") {
    Write-Host "Windows system detected. Running Windows commands..."

    # Step 1: Create a virtual environment
    python -m venv env

    # Step 2: Activate the virtual environment
    .\env\Scripts\activate

    # Step 3: Install dependencies
    pip install -r requirements.txt

    # Step : Capture the state of dependencies in requirements.txt
    pip freeze > requirements.txt

}
else {
    Write-Host "This script is for Windows. Use .\setup.sh for macOS/Linux."
    exit 1
}

