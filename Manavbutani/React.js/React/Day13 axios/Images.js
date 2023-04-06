import React from "react";
import Individual from "./Individual";

const Images = ({ images }) => {
  return images.map((image) => <Individual key={image.id} image={image} />);
};

export default Images;
