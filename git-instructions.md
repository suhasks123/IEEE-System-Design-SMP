# Instructions for using Git:

## Introduction:
We will have assignments throughout the SMP. For tracking and maintaining them, we will use Git. This will also help you get familiar with git and version control in general which is a very necessary skill if you want to build a career in Computer Science.

## Version Control:
It’s not necessary to learn this to understand git but it certainly helps. So imagine you’re working on a project in a team of like five people. How will you actually manage the code? Each person can’t be working on their own thing and expect the end result to like come together in the end somehow.

A natural way to resolve this is to have the leader of the project have the original code and all of the others have a copy. They work on their copy independently and when they create something significant, they report back to the leader and submit their work. The leader will review it and update the original code with the new code and send a copy of it to all the others. This is essentially version control.

You have a central repository containing the original code. Everyone on the team can see it, and copy it for working on their own. They make changes to it and update the original repository with the changes so that others on the team can see their changes. In this way, it keeps track of every change made to the original repository.

There are various version control systems like git, mercurial, etc. We’ll be focusing on git since it’s the most popular one.

## Git vs Github:

Git is the version control system. Github is a service that uses the git technology to host code online. So technically, github is a set of servers for hosting git repositories online for easier access.

## How to make Changes:

As we already discussed, there is a central repository or repo called the **remote repository** which contains the latest code with all the approved changes. Let’s look at the steps involved in making some changes to this. These steps are in the context of github since that’s what we’ll be using to host our repo.

All the assignments will be stored in a repository that both of us (the mentors) will have full access to. You will be able to view and fork this repository.

To make changes to this repository, there are a number of steps:

1. First **fork** the repository. This will create a copy of the original repository on your profile on github itself.

2. We clone the forked repository (the one on your profile) with:
```
    git clone <link-to-the-repo>
```
This creates a copy of the fork on the local machine. We can call this the **local repository**.

3. Each repository can have multiple **branches**. You can make changes to one of these branches without changing the others. So, there’s less chances of losing data by making some experimental changes. By default, every repo has a branch called the master. After you clone the repository, move to the main directory of the cloned repo(local) and run the following command to move to a new branch:
```
    git checkout -b "<new-branch-name>"
```
If there is an existing branch you need to move to, use the same command without `-b` with the name of the existing branch in place of `new-branch-name`. 

So, from now on, whatever changes you make will only be in the new branch that you have created.

4. We can make our required changes to the local repository. We can check the changed files using:
```
    git status
```
5. We then **stage** the changes using:
```
    git add <files-to-add>
```

You can stage all your changes using:
```
    git add .
```


Staging is essentially an intermediate step where we still have the option to choose what changes we need and what changes we don’t need to be updated in the local repo.

6. Once we have staged the changes, we **commit** them using:
```
    git commit -m "<commit-message>"
```
This is essentially saving your staged changes on your local repo in one single unit called a **commit**. Unstaged changes won’t be saved. Check your staged changes using `git status` before committing them since it’s problematic to change already committed changes, and also changing commits is not a good practice.

7. Committing your changes only saves them in your local repo. You need to **push** these changes to the forked repository:
```
    git push origin <branch-name>
```
If you want to push the changes to the master branch use `master` as the branch name.

8. Now your fork has the changes you want to make. Access the fork repo on github and click on **send pull request** to send a pull request to the remote repository controlled by us. We will then review your changes (the assignment) and **merge** them into the remote repo.


This is the basic git workflow. Use it to submit your assignments.
