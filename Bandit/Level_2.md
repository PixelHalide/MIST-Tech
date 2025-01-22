# Level 2

looking at the dashed filename, i know that the dash is a special character in bash, so i can't directly do cat -.

my first instinct was to do **cat "-"**, but even that doesn't work. i end up trying **cat ./-**, which does yield me the password.