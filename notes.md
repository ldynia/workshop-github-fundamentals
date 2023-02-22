# Presentation

## Introduction

### Who am I?

Good morning, good afternoon and good evening everyone. My name is Lukasz Dynowski and I'm an independent consultant located in Copenhagen, Denmark. Having over a decade of experience in IT I was involved in over hundreds of projects. I managed to work for a start-up, in academia and for a big organization working on premise and in the cloud. I managed to do work as a FullStack Developer, DevOps Engineer, Software Architect and more. The closest to my heart though is Backend in its full spectrum that is development and operations.

### About the workshop

So here I'm with around 10 years of experience with GitHub. Although, the title GitHub Fundamentals might sound trivial and well explored, you will be surprise that this workshop encapsulates several decades of software engineering. My goal is to show you how to create an open source project, how to contribute to an open source project, demonstrate you DevOps practices by utilizing GitHub actions, teach you how to create a microservice, and finally show you how you can use GitHub as a branding platform, so you can stand out from the crowd.

### Important

If you have any questions that cannot be answered during this workshop then don't be shy to drop me a message on the Linked in or just simply connect with me. Furthermore, it's important for us to deliver the best quality workshop, so please leave your feedback, so we can improve on it.

### Personal Note

On a personal note, I'd like to congratulate you for choosing O'Reilly as a learning platform, I believe it’s the shortest way to get access to various experts.

### Structured

Structure of this workshop consist of a short presentation and hands on exercises. I'm sure that this workshop will be blast for you and for me. Without further a do lets start the presentation.

## Open Source

```
AT&T Bell Labs  1970    Unix
GNU Project     1983    GNU
GCC + Libs      1987    GCC
4 Freedoms      1989    GPL
Linux Kernel    1991    Linux Kernel
Netscape        1998    Open Source
GIT             2005    GIT
GitHub          2008    GitHub
GitHub          2016    GitHub Universe
GitHub          2018    Acquisition $7.5 billion
```

1970s Unix - AT&T Bell Labs research center [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson), [Dennis Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie), started development of Unix - [Multics](https://en.wikipedia.org/wiki/Multics)-like operating system. Unix is license as a proprietary software that means creator or publisher of a software reserves some rights to use, modify, share modifications, or share the software.

1983 GNU ("GNU's Not Unix!") Project is created by [Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman) to create free a Unix-like operating system with source code that could be copied, modified, and redistributed (free/libre software). The work was funded by donations from individuals and companies to the [Free Software Foundation](https://www.fsf.org/about).

1987 GCC (GNU C Compiler/Compiler Collection ) 1.0 Released. - C compiler and collection of libraries.

1989 [GPL](https://www.gnu.org/licenses/old-licenses/gpl-1.0.html) (GNU GPL or GNU General Public License) is released for use with programs released as part of the GNU project. Licence give you four Freedoms: Freedom to run a program for any purpose, Freedom to study the mechanics of the program and modify it, Freedom to redistribute copies, and Freedom to improve and change modified versions for public use.

1991 LINUX Kernel - [GPL2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) licenses (28.8 million lines of code)

1998 Open Source -  [Open Source Initiative](https://opensource.org/) is founded by [Bruce Perens](https://en.wikipedia.org/wiki/Bruce_Perens) and [Eric Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond) to promote [open source movement](https://en.wikipedia.org/wiki/Open-source-software_movement). The term edged out "sourceware" and was coined by [Christine Peters](https://en.wikipedia.org/wiki/Christine_Peterson) to describe free software.

2005 GIT - Being dissatisfied with Source Control Management (SCM) system of that time, and inspired by workflow of [BitKeeper](https://en.wikipedia.org/wiki/BitKeeper) Linus Torvalds created GIT for purpose of development the Linux kernel.

2008 GitHub - Known as Logical Awesome LLC GitHub is founded.

[“Free software”](https://www.gnu.org/philosophy/free-sw.html) means software that respects users' freedom and community. Roughly, it means that the users have the freedom to run, copy, distribute, study, change and improve the software. Thus, “free software” is a matter of liberty, not price. To understand the concept, you should think of “free” as in “free speech,” not as in “free beer”. We sometimes call it “libre software,” borrowing the French or Spanish word for “free” as in freedom, to show we do not mean the software is gratis.

## Licenses - Permissive vs Copyleft

Permissive licenses allow you to copy, modify, recombine, and redistribute the work with minimal restrictions. Usually, only attribution is required. Copyleft provides the same permission as a permissive license, but requires you to release any derivative works you make under the same copyleft license.

| | Copyleft | Permissive |
| - | --- | ----------- |
| Linux | GPLv2 | - |
| Kubernetes | - | Apache 2.0 |
| GitLab | - | MIT |
| Mongo | SSPL*  | - |

---


# Technologies

## Git

Git is a source version control developed by Linus Torvalds.

## Markdown

Markdown is a markup language. The goal was to create an easy to read and write annotated text that can be optionally converted into HTML. Created by John Gruber and Aaron Swartz in 2004 (17 years old at the time).

## Docker

Docker is a containerization platform created by Solomon Hykes in 2013 (8 years ago). Containers are executable artifacts containing OS, OS's libraries, application source code and app's dependencies, movable as a docker images and described in a Dockerfile.

## Jekyll

Static site generator written by GitHub's co-founder Tom Preston-Werner in 2008. It takes Markdown as an input and produces static web page ready to be served by any HTTP server. It can be used with any front-end framework.

---

# GitHub

## 1. GitHub Repository

### What is a GitHub repository?

A repository is a place where your git project and its files resides. Typical repository stores source code along with .git folder - a directory which tracks snapshot of changes introduced to your files.

### Why to use GitHub repository?

GitHub repository is:

- A place for documenting your project - GitHub Wiki
- A place for automatizing tasks within software development life cycle - GitHub Actions
- A place for organizing and tracking work items - GitHub Projects
- A forum for sharing and raising questions - GitHub Issues
- A place for security scanning - GitHub Security
- And many more ...

### What is a GitHub template?

A GitHub Template is a way of marking your repository as a reusable blueprint. GitHub Template allows to generate new repositories that will preserve the same structure, branches and files as the blueprint repository.

## 2. Microservice

### What is microservice and why to use them?

Microservices/Microservice Architecture - is an architectural style that structures an application as a collection of services that are:

- Loosely coupled.
- Independently deployable.
- Highly maintainable and testable.
- Organized around business capabilities.
- Owned by a small team.

### What are typical features of microservice?

A typical microservice exposes following features:

- Is structured around business boundaries / bounded context
- Has independent database.
- Communicates over the network.
- Has well defined API.

## 3. GitHub Issues

### What are GitHub Issues?

GitHub Issues is a tool for keeping track of tasks, bugs and feedback for your project.

### Why to use GitHub Issues?

It's just a convenient way to manage all affairs related to your project.

## 4. GitHub Releases / Tags

It's very seldom that your software will be released only in one version, e.g. v1.0.0. As your project grows, you will have a bug to fix and feature to add. GitHub Releases allows you to create tagged artifacts of your software.

## 5. GitHub Actions

### What is GitHub Actions?

GitHub Actions is a tool that allows you to automate tasks within your software development life cycle. GitHub Actions are event-driven, which means that commands that you want to execute run after occurrence of a specified event.

### Why to use GitHub Actions?

GitHub Actions allows you to adopt backbone of DevOps methodology such CI/CD.

Explenation:

- **Continuous Integration** goal is to automatize tasks related to building, packagin, and testing application.
- **Continuous Delivery** goal is to automatize the delivery of applications to given environment (test or production) via manual release.
- **Continuous Deployment** goal is to automatize software release to a production environment - no manual.

## 6. GitHub Pull Request

### What is a Pull Request?

A pull request (PR) is a feature of a git hosting service that allows to create a contribution to the repository. PRs allow the maintainer of a repository to review, ask for comments, edit or even discard submitted work. I like to think of a PR as a **tangible unit of work in a collaborative world of code**.

## 8. GitHub Pages

### What is GitHub Pages?

GitHub Pages is a hosting service for static sites, it will serve any static files (HTML, CSS, JavaScript) that you push to repository. You can create your own website from static files, or use a static website generator such [Jekyll](https://jekyllrb.com/docs/).

### Why to use GitHub Pages?

The short answer is for **branding** and **promotion**. You can use it for blogging, or as a journal of your work. You can promote yourself with my_username.github.io or your project my_username.github.io/my_project. Moreover, you have option to brand your work with a custom domain.

## 9. GitHub Wikis

Wiki is an important part of an open source project. READEME.md is intended to be used as a brief documentation on how to get started with a project. Wiki on the other hand are intended to provide information about the project that can't be expressed by code.

--- 

# Links

- https://opensource.org/osd
- https://www.gnu.org/philosophy/free-sw.en.html
- https://www.youtube.com/channel/UCQvR8lgE9rishcKT_hZT6eQ
- https://en.wikipedia.org/wiki/License_compatibility#:~:text=The%20need%20for%20such%20a,and%20publish%20a%20new%20program.
- https://www.thehyve.nl/articles/open-source-software-licenses-part-3
