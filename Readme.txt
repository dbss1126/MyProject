소스코드 설명

game_record_a.py : 1세대의 경우 랜덤으로 1세대 개체를 생성한 후 그에 대한 데이터와 생존경쟁 데이터를 생성한 후 result-(세대번호).txt의 파일로 저장합니다. 2세대 이상의 개체에서는 세대의 데이터를 저장한 후 생존경쟁 데이터를 생성해 result-(세대번호).txt의 파일로 저장합니다

next_generation.py : 유전시킬 개체의 유전자를 입력하고 세대를 입력하면 다음세대의 개체 4개를 만들어 출력합니다

simulator_aa.py : 하디-바이엔베르크법칙 시뮬레이션을 위한 프로그램입니다. 개체수를 입력하고 거듭할 세대의 수를 입력해주면 세대별 대립유전자의 비율을 출력합니다