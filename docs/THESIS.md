## Key points:
* Shannon entropy 
* Rényi Entropy
* your own equations ($len^2 \times O \times H$)


# Methods
The main way to classify the strength of a password is by entropy.
In order to measure entropy, I have proposed a way of compression by tokenization, thus approximating
the entropy in a certain text.

## 1. Tokenization
Tokenization splits into 3 levels: Preset tokens, Repetitions, individual characters.
each password shall return a list of string tokens.

#### examples:
~~~
"password" -> ["password"]
"ilovecats123" -> ["i","love","cat","s","123"]
"iloooooovecatssssss" -> ["i","l","(o:6)","v","e","cat","(s:6)"]
~~~


## Individual tokens
Separate, individual characters are tokenized this way.
It is the most basic, primitive tokenization of all. 

The character simply gets its own token, whereas the [Enum value](../src/tokenization/enum.py) corresponds to its 
type (i.e. lowercase, uppercase, digit, etc.).



## Preset tokens
preset tokens are a hardcoded [JSON file](../src/tokenization/preset.json), 
with some common terms passwords commonly contain.
The value of each term corresponds to the [Enum value](../src/tokenization/enum.py), which is for all presets `1`.

All the preset tokens are non-case-sensitive (e.g `"qwerty"` = `"qWeRtY"`)



## Repetitions
Repeating characters or statements shall be marked as `(<char>:<occurances>)`.

I am currently conducting work on expanding repetitions to detect multi-character patterns
(e.g. `"ahahahah"` $=>$ `"(ah:4)"`).

### Preset token repetition
Preset token repetition occurs when and only when the same preset token appears twice or more in a row.
in which case, what would have been twice or more tokens, will now be reduced to one repetition token, of 
enum type `1` (preset token).

But that raises the question, what about repeating more than one preset term in order (e.g. `"qwerty123qwerty123"`)?


### Multi-character repetitions
For Multi-char repetitions, a length boundary must be drawn. No reasonable person would put 
`"hgfaskhgfask" -> "(hgfask:2)`, as it is on the same level with `"ahahahah" -> "(ah:4)"`. thus, I decided to
draw the line at $l_i = 4$, whereas if $l_i>4$ it shall not be interpreted as a repetition token, rather it would be
interpreted as a regular token.

For each type of repeating token, the enum value will be the same as the non-repeating type, with a few exceptions:
1. A multi char sequence shall have its own enum, as well as an additional `length` attribute.
2. A mixed sequence (i.e. multi-char with mixed symbol types) shall 



## Data analysis using the token list
In order to extract entropy from the token list, we use a couple of methods (which will come together at the end result). 

### Shannon entropy

$H= -\sum_i p(t_i) log_2(p(t_i))$
