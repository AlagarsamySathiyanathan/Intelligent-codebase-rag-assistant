import os
from dotenv import load_dotenv
load_dotenv()
import requests # to call GitHub api
# This script connects to GitHub

GITHUB_TOKEN=os.getenv("GITHUB_TOKEN") # Fetch GitHub token from environment

HEADERS={
    "Authorization": f"token {GITHUB_TOKEN}", # Proves identity to GitHub
    "Accept" : "application/vnd.github+json"   # Requests JSON response
}
# GitHub API requires authentication headers to avoid strict rate limits.
ALLOWED_EXTENSIONS = (".py",) # i want only python source files

# Function finds the default branch name of a github repository
def get_default_branch(owner, repo): # github user name eg.pallets and repository name eg.flask
    url = f"https://api.github.com/repos/{owner}/{repo}"   
    response = requests.get(url, headers=HEADERS) # Sends an authenticated GET request to GitHub
    response.raise_for_status()     # if github returns 404,403 error , fails program immediatly ,we can  to identify exactly where the prblm is . 
    return response.json()["default_branch"]

def get_repo_tree(owner,repo,branch): # fetch entire file structure of a repository in one API call
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    response=requests.get(url,headers=HEADERS)  # Sends authenticated request
    response.raise_for_status() # ensures API failures are caught early instead of silently breaking the pipeline.
    return response.json()["tree"] # O/p in json format


def fetch_file(owner,repo,branch,path): # Download actual source code os a file
    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    response=requests.get(raw_url)
    response.raise_for_status()
    return response.text # return pure code text


# Main Ingestion 
def ingest_repository(owner,repo): # function does, scans repo,filter file,,download code and prepare documents
    branch=get_default_branch(owner,repo)
    tree = get_repo_tree(owner, repo,branch)# full repo structure

    documents=[]

    for item in tree: # item is a file or folder
        if item["type"] != "blob":
            continue
        
        path=item["path"] 

        if path.endswith(".py"):
          # this ensures file is in important directories and python code
            try:
                content = fetch_file(owner, repo ,branch,path)
                documents.append({
                    "text": content,
                    "metadata": {"file_path": path,}
                })
            except Exception as e:
                print(f"Skipping {path}: {e}") # silently skip errors

    return documents


if __name__=="__main__":
    docs=ingest_repository("pallets","flask")
    print("File ingested:",len(docs))