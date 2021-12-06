# aCTFfinal Writeup

**Challenge 1 : norsa**

This one was a crypto challenge. Essentially, a unique set of encryption variables were used for signing a 40 char long note_id into a 308 char long token. The two values could then be used to read a note, the content of which, contained the flag. There was a function that allowed signing an arbitrary integer value into a token. the catch was that each important note_id began with '1111' as its first 4 digits and the signing function was designed to exit if the first 4 chars of the note_id were 1111.

The trick was to append a 0 at the beginning of the note_id. Now, the first 4 chars are no longer '1111' but '0111' but the integer value remains the same, giving us the right signed token caluclated using the encryption algorithm which we then used to retrieve flags.

Exploit - norsa.py
 
**Challenge 2 : notemanager**

This was a simple one, a backdoor variable called 'backd00r' could be exploited using command injection. We set its value to 'ls' to simply list files, the names of which, contained flags.

Exploit - notemanager.py

**Challenge 3 : cyper**

This was a command injection challenge as well, we used the vulnerability to print sqlite database files and read flags.

Exlpoit - cyper.py

Note - There were a few other challenges as well that we solved partially or could not automate in time.
