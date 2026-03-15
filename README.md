# What is Git?

- Git is an open source Version Control System. It is used to track the changes in code in different versions during software development.
- All of the versions are stored in a Git repository, in a .git folder.
- Git allows developers to have local copies of the different versions in the history of the project.
- Github is a cloud-based platform that acts as an interface for Git.

# How to push code to GitHub
- Pushing code to github means uploading the code you have on your computer to a Git repository which creates an online copy of your code, making it possible for others online to access your code.
- To push code to GitHub, you have to first create a GitHub account.
- You can either push the code through the web interface, code editors, or through the command line on your computer.
## How To push code through the Command Line Interface
1. Make sure that you have git installed on your computer.
2. Open terminal and navigate to your project folder and run `git init`.
3. Prepare your files for the commit(uploading) by running `git add .` which prepares all the files in the directory.
4. Save the staged changes to your local history by running `git commit -m "Initial commit"`.
5. Copy the repository URL and run `git remote add origin <URL>`.
6. Finally, push the code by running `git push -u origin main`.

# What is Markdown?
- Markdown is a markup language used to format plain text, making it easier to read, write, and convert to HTML.
- Using HTML for formatting text can be cumbersome for some people, that's where markdown is used.
## Basic Markdown Syntax
1.### Headings(#): The '#' symbol is used to denote headings. '#' creates Heading1, '##' creates Heading2, etc. in a hierarchical manner.
2.### Bold and Italic: Use '*' or '_' to make the text italic or '**' or '__' to make the text bold. Use '***' or '___' to make the text bold and italic.
3.### Lists: '-' is used for bullet points and '1.', '2.', etc. are used for numbered lists.
  
