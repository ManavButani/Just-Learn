import React, { Component } from "react";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "",
      final: null,
    };
  }

  data = [
    {
      dname: "Manav",
      password: "123",
    },
    {
      dname: "Krenil",
      password: "1213",
    },
    {
      dname: "Shyam",
      password: "1234",
    },
    {
      dname: "Krupal",
      password: "456",
    },
  ];

  input_on_page = (event) => {
    // console.log("Inside input_on_page");
    this.setState({ name: event.target.value });
  };

  submit_on_page = (event) => {
    // console.log("Inside submit_on_page");
    event.preventDefault(); // restrict to refresh a page
    const user = this.data.find((user) => user.dname === this.state.name);
    // data is our list/array
    // find is inbuilt method
    // which takes function as a argument
    // return value based on function condition
    // if function doesn't satisfied condition then returns null

    if (user) {
      //   console.log("Inside IF");
      //   console.log(user);
      this.setState({
        final: user.dname,
      });
    } else {
      //   console.log("Inside ELSE");
      this.setState({ final: null });
    }
  };

  render() {
    return (
      <>
        <form>
          <div>
            <input
              placeholder="Enter Your Name:"
              type="text"
              value={this.name}
              onChange={this.input_on_page}
            ></input>
            <button type="submit" onClick={this.submit_on_page}>
              Submit
            </button>
          </div>
        </form>
        {this.state.final ? <h1>Welcome, {this.state.final}</h1> : null}
      </>
    );
  }
}

export default App;
