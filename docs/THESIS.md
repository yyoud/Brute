## Key points:
* Shannon entropy 
* Rényi Entropy
* comparison and method recite to zxcvbn 


# Methods
The main way to classify the strength of a password is by entropy.
In order to measure entropy, I have proposed a way of compression by tokenization, thus approximating
the entropy in a certain text.

This algorithm tries to generally mimic the [zxcvbn password strength detection algorithm](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/wheeler),
without copying any code at all.
Thus, it will be compared to it, before the training of the neural network, 

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

### Substitution



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

---

# Data analysis using the token list
In order to extract entropy from the token list, we use a couple of methods (which will come together at the end result).

## Shannon entropy
[Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))
is a formula from information theory, designed to give an orderless entropy index.
I use it here to calculate a few indexes, thus giving me some ideas of general entropy
in the password.

That being said, it CANNOT be used independently, since it doesn't magnify character order at all.

The formula for binary shannon entropy is:
$$H= -\sum_{i=0}^{L-1} p(P_i) \times log_2(p(P_i))$$

Where: \
$p(P_i)$ is the probability of token $P_i$ in the given text.

### Diversity
the diversity of a certain character field in a text, is calculated
via the [Enum value](../src/tokenization/enum.py) of the token.
The probability is taken on the [Enum value](../src/tokenization/enum.py) in this case.
We mark the diversity as $D(p)$.

### Orderless Entropy Index (OED)
The Orderless Entropy Index, is the shannon entropy taken on each token's raw value.
The probability is taken by iterating once over the token list, and counting the occurrence of
each token value.
It shall be marked as $\displaystyle OED(P^*)$.

<!--
i need to do this on the token types (enum) and the token values. also i need to start calculating costs.
and also try to finish theory and start coding before may 5th more or less (after major exams) 
-->

## Keyboard patterns
Keyboard patterns are patterns pretty intuitive. a password such as `"dfghjk"`, that creates a line on a keyboard, 
is not gonna be as secure as an obscure password, scattered over the keyboard.

I propose a way to efficiently detect such patterns, as well as their linearity:
**Geometrical Spatial Analysis**.

Let the keyboard be a coordinate system, the origin being the first char of the passsword $P_0$. \
Let $M(d, C)$ be a domain-relative vector preset map (assuming qwerty keyboard), where d is the domain, and C is the character.

For each character $P_i$: \
Taken the next char $P_{i+1}$, we conduct a search in the map, using the domain $P_i$: \
$$v_i = M(P_i, P_{i+1})$$

let $L = length(P)$ \
let $V_T$ be the net displacement.
$$V_T = \sum_{i=0}^{L-1}(v_i)$$

The slope of which cancels nicely to:
$$m_{V_T} = \frac{y_{P_L}}{x_{P_L}}$$
Then resulting in the discriminant:
$$y'(p_i) = m_{V_T} \times x_{p_i}-y_{p_i}$$

To calculate the linearity of the pattern, we need to calculate the **Displacement-Normalized Area (DNA)**, which is
the sum of the absolute values of all the $V_T$ relative 
areas trapped in the piecewise-linear loop we have.
To do this, we can use the **Shoelace Formula**:

$$DNA(P)=\frac{1}{2}\sum_{i=0}^{L-1}(\lvert x_{P_i} \times y'_{P_{i+1}} - x_{P_{i+1}} \times y'_{P_i} \lvert)$$


