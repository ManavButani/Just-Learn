import React from "react";
import PropTypes from "prop-types";

const Styler = (props) => {
  return (
    <div>
      <div className="card" style={{ width: "18rem ", fontWeight: "bold" }}>
        <div
          className="card-body"
          style={{
            fontWeight: "bold",
            fontFamily: "Times New Roman",
            display: "inline-block",
          }}
        >
          <h5 className="card-title">App Id: {props.product.id}</h5>
        </div>
        <ul className="list-group list-group-flush">
          <li className="list-group-item">{props.product.app}</li>
          <li className="list-group-item">{props.product.name}</li>
          <li className="list-group-item">
            {props.product.pinned ? (
              <input
                type="checkbox"
                data-toggle="toggle"
                checked
                data-onstyle="outline-success"
                data-offstyle="outline-danger"
              />
            ) : (
              <input
                type="checkbox"
                data-toggle="toggle"
                data-onstyle="outline-success"
                data-offstyle="outline-danger"
              />
            )}
          </li>

          <li className="list-group-item">
            {props.product.silent ? (
              <input
                type="checkbox"
                data-toggle="toggle"
                checked
                data-onstyle="outline-success"
                data-offstyle="outline-danger"
              />
            ) : (
              <input
                type="checkbox"
                data-toggle="toggle"
                data-onstyle="outline-success"
                data-offstyle="outline-danger"
              />
            )}
          </li>
        </ul>
      </div>
    </div>
  );
};

Styler.propTypes = {
  product: PropTypes.object,
};
export default Styler;
