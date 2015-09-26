# Tickler

I follow the GTD methodology to keep my life in order. GTD advocates the use of a tickler file in which you place papers that your future self will need. 

I've moved almost entirely to a paperless workflow so I no longer need a physical tickler file. However, I do need to send myself things in the future from time to time. 

Enter Tickler

Tickler is a simple python script that runs via cron or your favorite method and watches a directory. Any files that have a future date in the file name are emailed on the date they are due. 

How I use it?

I have TextExpander plus Hazel to help me work with my Tickler files.

All incoming Scans go into a folder on my hard drive.

I use TextExpander to create common files names. In this case **tickler - duedate - description**

Then, I use Hazel to move those incoming files into the appropriate watch folder.

Tickler then runs everyday at 6:00am emailing me the days files. 

## Installation

### Dependencies

Tickler requires the following installed:
* dateutil
* json


## Usage

Usage is pretty simple. 

Create the directory .tickler in your home directory.
Copy config.json-example as config.json into your home directory.
Edit the file, filling in email information and the tickler folder diretctory.

Then, setup cron or launchctl to run the script everday at a specific time. 


## Support

Please [open an issue](https://github.com/JoeCotellese/tickler/issues) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/JoeCotellese/tickler/compare/).
