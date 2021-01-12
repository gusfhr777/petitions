# petitions
* 국민청원 링크 입력시 자동으로 댓글을 읽어주는 프로그램 입니다.
* CORS 정책 때문에 /api/agreement_list/(게시물 번호)에서 POST요청이 불가능합니다. 이로인해 사전 검토가 끝난 청원 게시물의 댓글 탐지 속도가 "매우" 느리다는 점 양해바랍니다.
* 실행이 안 될시 exe가 포함된 폴더에 자신의 크롬 브라우저 버전을 확인한 후, chromedriver.exe 파일을 다운받아 설치하시기 바랍니다. chromedriver.exe 파일 다운로드는 https://chromedriver.chromium.org/downloads에서 가능합니다.

-- update
* 관리자가 검토중인 청원 이외에 검토 허가된 청원의 댓글도 읽을 수 있게 하였습니다.

-- update 2
* threading모듈을 이용해 개선된 속도로 이용할 수 있습니다. thread사용은 2를 추천합니다. thread 갯수가 두 개 이므로 이론상 두배의 속도를 보증합니다. 하지만, thread 갯수를 너무 많이 늘릴 시 잠시 후 이용하라는 alert가 출력되므로 속도의 한계는 분명 존재합니다.
* chromedriver_autoinstaller모듈을 exe파일에서 이용시 오류를 내뿜기에 부득이하게 사용을 중단(...)할 뻔 하다가 폴더생성이 안 되서 발생하는 오류인 것을 인지하여 이를 수정해주도록 fixlr.py를 생성하였습니다.
