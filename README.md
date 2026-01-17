# adtelligent_test_task


## How to run tests locally:
1. Create virtual environment:
```
python -m venv venv
```
2. Activate virtual environment:
```
.\venv\Scripts\activate
```
3. Install required modules.
```
pip install -r .\requirements.txt
```
4. Create `.env` file and set variable:
```
FAVQS_TOKEN=your_api_token
```
The tests will automatically read this token using python-dotenv.

5. Run tests.
```
pytest
```

Tests can also be run in GitHub Actions on push or pull_request.
API token is stored securely as a repository secret (FAVQS_TOKEN) in GitHub Actions.