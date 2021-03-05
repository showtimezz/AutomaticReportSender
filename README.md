# Automatic Reported Sender

A simple, standalone Python app that attaches PDF-s, images and text to an email, and automatically sends it to another email adress. 

## Getting Started

This app takes all files located in the `/images` and `/pdfs` directories, attaches them as such to an email message. Text is hardcoded to the `msg.set_content()` variable. 

### Prerequisites/Dependencies



```
Python 3.x
pip
os
smtplib
imghdr
datetime 
email
```

### Installing

To get started with using this bot, run `git clone git@github.com:showtimezz/AutomaticReportSender.git` from your terminal. 


## Deployment

You can run this program with `python mailSender.py` directly from a terminal, given that the program is at least symlinked to the root directory. Alternatively, you could add a bash alias and run it from there without having to specify the path to the script every single time. [This article](https://opensource.com/article/19/7/bash-aliases) explains how to do that.

## Contributing

The easiest way to contribute to the development of this program is to take a quick look at the [Issues page](https://github.com/showtimezz/AutomaticReportSender/issues). 




## License

This project is licensed under the MIT License.

