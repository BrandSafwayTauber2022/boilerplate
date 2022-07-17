##### Author
Joshua Fink
joshfink@umich.edu


# boilerplate
Standard .gitignore and .pre-commit-config.yaml files to use with BrandSafway projects. Also contains a sample pytest setup.

## Quick Start
To get started quickly, follow these simple steps to run an automated bash script:

### 1. Clone the boilerplate repository
<p><code>  git clone https://github.com/BrandSafwayTauber2022/boilerplate.git  </code></p>

### 2. Enter the boilerplate directory
<p><code>  cd boilerplate  </code></p>

### 3. Make the automated bash script executable
<p><code>  chmod +x bin/setup_wsl  </code></p>

### 4. Create empty GitHub repository for new project and copy URL
Click the green "New repository" button in the image below and follow on screen prompts.

![image](https://user-images.githubusercontent.com/49216284/179423914-4f6c2941-24ba-40b4-a9a4-79175ffe6770.png)

Copy the HTTPS url in "Quick setup". This HTTPS url will placed in lieu of  <code>[GITHUB_REPO_HTTPS_URL]</code>  in the next step. DO NOT execute any of the other commands seen in the image below.

![new_repository](https://user-images.githubusercontent.com/49216284/179423775-92d3c696-1c9f-42d5-9497-014ab85953b5.png)

### 5. Run bash script and follow command-line prompts
<p><code>  ./bin/setup_wsl [GITHUB_REPO_HTTPS_URL] </code></p>

#### Example 
<p><code>  ./bin/setup_wsl https://github.com/BrandSafwayTauber2022/example.git </code></p>

