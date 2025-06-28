![image](https://github.com/user-attachments/assets/619035fc-5c3f-4a47-a0d3-b9acdbba1198)



waves over lambda

cloud shell

i used the terminal of the cloud shell 

i ran this command first 

sudo apt install netcat-openbsd -y
 
to download nc 


then i ran the command that was given 

nc jupiter.challenges.picoctf.org 39894


it gave me this 

imskrvtl hdrd ql bmur exvk - erdgudsib_ql_i_mndr_xvfwov_vkexiktbud
-------------------------------------------------------------------------------
zd zdrd smt fuih fmrd thvs v guvrtdr me vs hmur mut me mur lhqp tqxx zd lvz hdr lqsc, vso thds q usodrltmmo emr thd eqrlt tqfd zhvt zvl fdvst wb v lhqp emusodrqsk qs thd ldv.  q fult vicsmzxdokd q hvo hvroxb dbdl tm xmmc up zhds thd ldvfds tmxo fd lhd zvl lqscqsk; emr ermf thd fmfdst thvt thdb rvthdr put fd qstm thd wmvt thvs thvt q fqkht wd lvqo tm km qs, fb hdvrt zvl, vl qt zdrd, odvo zqthqs fd, pvrtxb zqth erqkht, pvrtxb zqth hmrrmr me fqso, vso thd thmukhtl me zhvt zvl bdt wdemrd fd.
then i used cipher identifier 

https://www.dcode.fr/cipher-identifier


after analyzing it turned out to be substitution cipher 


so i used substitution cipher decoder 
https://planetcalc.com/8047/


and i got my flag 
FREQUENCY_IS_C_OVER_LAMBDA_AGFLCGTYUE

![image](https://github.com/user-attachments/assets/4022f7ec-b2ed-4dae-98f5-a9761ed6b3b8)
