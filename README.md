
## Data

### User

- Username
- First name
- Last name
- email
- password

### Account

- Biography
- Location
- website
- Date of birth
- Profile picture
- Background picture
- Creation date


### Follow

- Following FK (User)
- Followers FK (User)

### Twitt

- Author FK(User)
- Creation date
- Update date
- Twitt

### Comment

- Author FK(User)
- Creation date
- Update date
- Comment

### Like

- Author (User)
- Creation date
- Update date
- Comment FK(Comment)


### Retwit

- Author (User)
- Creation date
- Update date
- Twitt FK(Comment)

