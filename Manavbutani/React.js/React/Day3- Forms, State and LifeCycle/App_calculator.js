import React, { Component } from "react";
import "./index.css";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      string: "",
    };
  }

  handleButton = (event) => {
    this.setState({ string: this.state.string + event.target.value });
  };

  handleCalculate = () => {
    this.setState({ string: eval(this.state.string) });
  };
  handleClear = () => {
    this.setState({ string: "" });
  };
  render() {
    return (
      <>
        <div className="row">
          <input
            className="input"
            type="text"
            value={this.state.string}
            onChange={(e) => {
              this.setState({ string: e.target.value });
            }}
          />
        </div>
        <div className="row">
          <button className="button" value={7} onClick={this.handleButton}>
            7
          </button>
          <button className="button" value={8} onClick={this.handleButton}>
            8
          </button>
          <button className="button" value={9} onClick={this.handleButton}>
            9
          </button>
          <button className="button" value={"*"} onClick={this.handleButton}>
            *
          </button>
        </div>
        <div className="row">
          <button className="button" value={4} onClick={this.handleButton}>
            4
          </button>
          <button className="button" value={5} onClick={this.handleButton}>
            5
          </button>
          <button className="button" value={6} onClick={this.handleButton}>
            6
          </button>
          <button className="button" value={"/"} onClick={this.handleButton}>
            /
          </button>
        </div>
        <div className="row">
          <button className="button" value={1} onClick={this.handleButton}>
            1
          </button>
          <button className="button" value={2} onClick={this.handleButton}>
            2
          </button>
          <button className="button" value={3} onClick={this.handleButton}>
            3
          </button>
          <button className="button" value={"+"} onClick={this.handleButton}>
            +
          </button>
        </div>
        <div className="row">
          <button className="button" value={0} onClick={this.handleButton}>
            0
          </button>
          <button className="button" value={"."} onClick={this.handleButton}>
            .
          </button>
          <button className="button" onClick={this.handleCalculate}>
            =
          </button>
          <button className="button" value={"-"} onClick={this.handleButton}>
            -
          </button>
          <button className="button" value={""} onClick={this.handleClear}>
            C
          </button>
        </div>
      </>
    );
  }
}

export default App;
