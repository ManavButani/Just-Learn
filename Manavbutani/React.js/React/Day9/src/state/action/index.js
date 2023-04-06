export const redirectToSuccessPage = () => {
  return {
    type: "SUCCESS",
    payload: "http://localhost:3000/success",
  };
};

export const redirectToErrorPage = () => {
  return {
    type: "ERROR",
    payload: "http://localhost:3000/error",
  };
};

export const redirectToWrongPassword = () => {
  return {
    type: "WrongPassword",
    payload: "http://localhost:3000/wrongpass",
  };
};
