function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
  }
  
  // Obtén el valor de 'mail' desde la URL
  const mailFromUrl = getQueryParam('mail');
  
  console.log(mailFromUrl);