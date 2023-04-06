import React from "react";

const Individual = ({ image }) => {
  return (
    <div key={image.id}>
      <img src={image.urls.small} alt="Unsplash" />
    </div>
  );
};

export default Individual;
