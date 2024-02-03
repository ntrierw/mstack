# Mstack

Mstack is a simple and minimalistic static site generator that lets you create beautiful websites from Markdown files. It's fast, lightweight (1KB!), and easy to use.

## Installation

To install Mstack, you need to have Python installed on your system. Then, run the following command:

<!-- start:code block --> pip3 install markdown<!-- end:code block -->

## Usage

The `content` folder contains your Markdown files that will be converted into HTML pages. The `template` folder contains your HTML template that will be used to render your pages.

To build your website, run the following command:

<!-- start:code block --> python3 generate.py<!-- end:code block -->

This will generate files in the `output/content` folder with your static website files that you can deploy to any hosting service.

## Features

Mstack has the following features:

- **Markdown support**: You can write your content in Markdown, a simple and expressive syntax that makes writing easier and more enjoyable.
- **Custom layout support**: You can define your own HTML template for different types of pages, such as home page, blog post, or contact page.
