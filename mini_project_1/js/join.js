// 폼 요소를 선택 : document.querySelector('선택자')
// 지금 단계에서 알아야 하는 선택자는 3가지입니다.
// 요소 이름: div, form, a 등등.... 해당 요소가 페이지에 단 한 개뿐일 때 주로 사용
// id: #container, #submit-btn
// class: .item, .list
const form = document.querySelector('#form_container');

// getUserInfo라는 이름의 함수
// 각종 데이터를 전달 받아 객체의 형태로 만들어 반환합니다.
function getUserInfo(name, ssn_front, ssn_back, username, password, emailId, mailbox, address, gender, agree) {

  // 전달받은 데이터를 객체({})로 변환하는 과정
  const userInfo = {
    name: name,
    ssn: ssn_front + '-' + ssn_back,
    username: username,
    password: password,
    email: emailId + '@' + mailbox,
    address: address,
    gender: gender,
    agree: agree,
  };
  return userInfo;
}

// 폼 제출 이벤트 리스너 추가
form.addEventListener('submit', function (event) {
  event.preventDefault();
  const name = document.querySelector('#name').value;
  const ssn_front = document.querySelector('#ssn_front').value;
  const ssn_back = document.querySelector('#ssn_back').value;
  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;
  const passwordRetype = document.querySelector('#password-retype').value;
  const emailId = document.querySelector('#email').value;
  const mailbox = document.querySelector('#mailbox').value;
  const address = document.querySelector('#address').value;
  const gender = document.querySelector('input[name="gender"]:checked').value;
  const agree = document.querySelector('#agree').checked;

  if (username.length < 4 || username.length > 8) {
    alert('아이디는 4자 이상, 8자 이하로 입력하세요.');
  } else if (password !== passwordRetype) {
    alert('비밀번호가 일치하지 않습니다.');
  } else {
    const result = getUserInfo(name, ssn_front, ssn_back, username, password, emailId, mailbox, address, gender, agree);
    console.log(result);
  }
});
