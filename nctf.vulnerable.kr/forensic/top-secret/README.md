# Top Secret

## Forensic - Points: 1

> 적국의 일급 기밀이 담긴 가상머신 파일을 탈취하였다. 그러나, USB 메모리의 용량 부족으로 어쩔 수 없이 제일 중요해보이는 메모리만 덤프해 신속하게 현장을 탈출하였다. 적국의 기밀은 무엇인가?
>
> (Fake Flag파일이 존재합니다.)
>
> 
>
> He stole the virtual machine file containing the top secret of the enemy country. However, due to the shortage of USB memory, I dumped only the memory that seemed to be the most important. What is the secret of an enemy country?
>
> (Fake Flag file exists.)
>
> 
>
> Author: 신재욱(Y311J)
>
>
> [Download](https://drive.google.com/file/d/1eQMKWR8y-c2zPzqZFmncj0h8S7advhSm/view?usp=sharing)
>

	$ strings Windows\ 7\ Enterprise\ K-b94208dd.vmem | grep -i KorNewbie

flag: `KorNewbie{OH..You_Know_B4sic_0F_M3mory_Forensics!}`