# Group 1

 *Members:*

 - Luis Vazquez
 - Landon Brown
 - Kendall Lawson
 - Gavin Grady

## Project Management Tools

 *Atlassian Jira*
 - https://luisgvazquez.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog


## Commmunication Tools
*Microsoft Teams*
- https://teams.microsoft.com/l/channel/19%3ADYcUuSjcvCI-eA39mqTVg7ur5DsJSGhMAFOxbh6MC5k1%40thread.tacv2/General?groupId=e3b61ff2-7072-4d64-9c95-797850a824e4&tenantId=

## Project Flowchart 

```mermaid
flowchart TD;
    A[Start] --> B[Input YouTube video URL]
    B --> C{Choice: A/V?}
    C -->|A for Audio| D([Input audio quality])
    C -->|V for Video| E([Download video])
    D --> F{Quality: High/Low?}
    F -->|High| G([Download audio -High quality])
    F -->|Low| H([Download audio -Low quality])
    G --> J[Play audio]
    H --> J
    E --> I([Download completed])
    I --> K{Playback option?}
    K -->|Internal player| L([Play video/audio internally])
    K -->|External player| M([Open video/audio with external player])
    K -->|No playback| N[End]
    J --> O{Adjust playback settings?}
    O -->|Yes| P([Open playback settings])
    O -->|No| N
    P --> Q([Adjust settings])
    Q --> O
    B -->|Invalid URL| N([End])
    L --> N
    M --> N
```

## Instructions (will be updated as project evolves)

*Install Instructions:*
- Install python
- Install pip3
- Create virtual environment
- Activate virtual environment
- Install requirements.txt file
- Run main python file

*Use Instructions:*
- When it asks for link provide url for youtube video
- When it asks for audio or video: Type a or v
  - If A is selected, select quality and type in High or Low, video will be converted and downloaded as an mp3 audio file
  - If V is selected video will be downloaded as an mp4 video file
- When it asks you if you want to download another video
  - If you select yes, the process will start again
  - If you salect no the program will exit



