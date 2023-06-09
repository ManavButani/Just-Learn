import React, { Component } from "react";

export default class ErrorBoundaries extends Component {
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }
  static getDerivedStateFromError(error) {
    return {
      hasError: true,
    };
  }

  render() {
    if (this.state.hasError) {
      return <h1>Invalid Credentials</h1>;
    }
    return this.props.children;
  }
}
