const checkTheCredential = (state = "/", action) => {
  switch (action.type) {
    case "SUCCESS":
      window.location.href = action.payload;
      return "";

    case "WrongPassword":
      window.location.href = action.payload;
      setTimeout(() => {
        window.location.href = "/";
      }, 5000);

      return "0";

    case "ERROR":
      window.location.href = action.payload;
      setTimeout(() => {
        window.location.href = "/";
      }, 5000);

      return "1";

    default:
      return "2";
  }
};

export default checkTheCredential;
