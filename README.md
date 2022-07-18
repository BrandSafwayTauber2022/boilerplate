# boilerplate
Standard .gitignore and .pre-commit-config.yaml files with sample pytest setup for new BrandSafway projects.

#### Author
Joshua Fink, joshfink@umich.edu

## Latest boilerplate Updates
Run  <code>git pull</code>  in an existing cloned boilerplate repository to get the latest boilerplate updates.

## Quick Start
To get started quickly, follow these simple steps to run an automated bash script:

### 1. Clone boilerplate repository
<p><code>  git clone https://github.com/BrandSafwayTauber2022/boilerplate.git  </code></p>

### 2. Enter boilerplate directory
<p><code>  cd boilerplate  </code></p>

### 3. Make automated bash script executable
<p><code>  chmod +x bin/setup_wsl  </code></p>

### 4. Create empty GitHub repository for new project and copy URL
Click the green "New repository" button in the image below and follow on screen prompts.

![image](https://user-images.githubusercontent.com/49216284/179423914-4f6c2941-24ba-40b4-a9a4-79175ffe6770.png)

Copy the HTTPS url in "Quick setup". This HTTPS url will placed in lieu of  <code>[GITHUB_REPO_HTTPS_URL]</code>  in the next step. DO NOT execute any of the other commands seen in the image below.

![new_repository](https://user-images.githubusercontent.com/49216284/179423775-92d3c696-1c9f-42d5-9497-014ab85953b5.png)

### 5. Run bash script and follow command-line prompts
<p><code>  ./bin/setup_wsl [GITHUB_REPO_HTTPS_URL] </code></p>

Note: Some of the command-line prompts are intentionally scary, but if  <code>[GITHUB_REPO_HTTPS_URL]</code>  is empty there will be no issues :)

#### Example 
<p><code>  ./bin/setup_wsl https://github.com/BrandSafwayTauber2022/example.git </code></p>

## Concise Documentation

### .gitignore
All directories and files listed in this file are ignored when pushing to .git. This file ensures <code>env/</code> directory (where virtual environments are stored) do not get pushed to GitHub. While this would not cause issues if the GitHub repository was accessed by one computer only, it causes nightmares if the repository is accessed among multiple computers. It is advised to not modify this file.

### .pre-commit-config.yaml
Upon setup, this modifies .git/hooks/, and it contains a series of code quality checks. If any of these tests fail, local updates will not push to GitHub. To push to GitHub, fix issues noted on the command line, save the fixed files, and run  <code>git add .</code>  and  <code>git commit -m [UPDATE_MESSAGE_HERE]</code>  again until all are "PASSED" or "SKIPPED". Some of the pre-commit hooks actually fix the code for you, so sometimes simply re-running <code>git add .</code>  and  <code>git commit -m [UPDATE_MESSAGE_HERE]</code>  will do the trick. To use alone in a existing project, copy the <code>.pre-commit-config.yaml</code> file and run the following commands (assuming your virtual environment is installed):

<p><code>  pip install pre-commit  </code></p>
<p><code>  pre-commit install  </code></p>

Then, run the following command to ensure your current files meet pre-commit standards:
<p><code>  pre-commit run --all-files  </code></p>

Note: The autoformatting may not produce the ideal format in every single case. However, by using opinionated formatters, it will make BrandSafway code on the aggregate more readable.

Full documentation can be found here: https://pre-commit.com/

### pytest
A sample pytest setup is provided in the boilerplate code. Basic things to know:

1) The  <code>tests/</code>  folder must have an empty  <code>\_\_init\_\_.py</code> file.
2) Test classes must start with "Test", and test functions must start with "test_". Leave all test files explicitly in <code>tests/</code>.
3) Run pytest on the command line in the root of the repository using the following command: <code>pytest tests/</code>

Full documentation can be found here: https://docs.pytest.org/en/7.1.x/
