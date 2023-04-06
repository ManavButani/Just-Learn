import axios from "axios";
import React, { useState } from "react";
import Images from "./Images";

const App = () => {
  let [images, setImages] = useState([]);
  let fetchApi = async () => {
    const response = await axios.get(
      "https://api.unsplash.com/photos/?client_id=Zgb7syy6VpbUMgOfOZ41z-BlUL5y9ek_NT9gEaJS4y8"
    );
    // console.log(response.data);
    setImages(response.data);
  };

  return (
    <div>
      <button type="submit" onClick={fetchApi}>
        Images
      </button>

      {images.length > 0 && <Images images={images}></Images>}
    </div>
  );
};

export default App;
