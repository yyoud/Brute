<h1 align="center" >PlosionKit</h1>

<p align="center">A deterministic password strength meter</p>

# Methods
The main way to classify the strength of a password is by entropy.
In order to measure entropy, I have proposed a way of compression by tokenization, thus approximating
the entropy in a certain text.

## 1. Tokenization
Tokenization splits into 3 levels: Preset tokens, Repetitions, individual characters.
each password will return a list of string tokens.

#### examples:
    "password" -> ["password"]

    "ilovecats123" -> ["i","love","cat","s","123"]

    "iloooooovecatssssss" -> ["i","l","(o:6)","v","e","cat","(s:6)"]
""

### Preset tokens
preset tokens are a hardcoded [JSON file](src/tokenization/preset.json), 
with some common terms passwords commonly contain.
The value of each term corresponds to the <idk really>.


### Repetitions
Repeating characters will be marked as `(<char>:<occurances>)`

$H= -\sum_i p(t_i) log_2(p(t_i))$
