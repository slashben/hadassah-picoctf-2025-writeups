Hint : "Remember that cipher we devised together Squeexy? The one that incorporates your affinity for linear equations???"

Once we connected to the server using cmd we presented with a message which includes the following details:
 
secret cheese :  LQJKWVRSE
Hint from the server : "The cheeses are top secret and limited addition, so they might look different from cheeses you're used to! "
commands : (g)uess my cheese or (e)ncrypt a cheese.

We have 3 tries to prove that we are Squeexy

- The first thing I would like to try is to encrypt a cheese to see what comes up, I can only use 2 because in the 3rd try I have to guess the cheese.
Aragon -> WLWMQJ
A -> W 
R -> L 
A -> W 
G -> M 
O -> Q
N -> J

Ardrahan -> WLRLWTWJ
A -> W
r ->L
d ->R
r -> L
a ->W
h -> T
a -> W
n -> J

We can see that A=W, R= L , and the hint says "affinity for linear equations" so I'm assuming this is Affine Cipher.


I created Liner equsions to use them for calculating the rest of the letters:
A = W -> O = 22
R = L -> 17 = 11

22 = O*m + b (mod 26) -> b = 22
use b=22 here :
11 = 17m + 22 (mod 26)

now we get :
y≡7x+22 , wehre m=7, b=22

lets see if its correct by calcultaing a letter from "Ardrahan" ,we use "H=7", to check if its indeed being encrypted to "T =19"
y≡7x+22 - > X = 7
y = 7*7 +22 (mod 16)
y = 19 
So we indeed got 19/T - so this is hoe we are gonna decrypt the secrete cheese

---------------------------------
R->L
y≡7x+22 -> y=11
X= 17

O->Q
y≡7x+22 -> y =16
X= 14

N->J
y≡7x+22 -> y = 9
X= 13

C->K
y≡7x+22 -> y =10
X= 2

A->W

L->V
y≡7x+22 -> y =21
X=11

D->R
y≡7x+22 -> y =17
X=3

S->S
y≡7x+22 -> y =18
X=18

Q->E
y≡7x+22 -> y =4
X=16

The decrypted cheese : RONCALDSQ
The flag : picoCTF{ChEeSy6320b114}
