import React, { Component } from 'react';
import PropTypes from 'prop-types'

import './counter.css'

class Counter extends Component {
  constructor() {
    super();
    this.state = {
      counter: 0
    }
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.reset = this.reset.bind(this);
  }
 


  render() {
    return (
      <div className="Counter">

        <CounterButton by={5} incrementMethod={this.increment} decrementMethod={this.decrement}/>
        <CounterButton by={10} incrementMethod={this.increment} decrementMethod={this.decrement}/>
        <CounterButton by={15} incrementMethod={this.increment} decrementMethod={this.decrement}/>
        <span className="count">{this.state.counter}</span>
        <div><button className="reset" onClick={this.reset}>Reset</button></div>
        
      </div>
    );
  }
  increment(by) {
    //increment from child -${by}
    this.setState(
    (prevState)=>  {
       return  {counter: prevState.counter + by}
      }
    );
  }
  decrement(by) {
    //increment from child -${by}
    this.setState(
    (prevState)=>  {
       return  {counter: prevState.counter - by}
      }
    );
  }

  reset()
  {
    this.setState(
       
          {counter: 0}
        
      );
  }

}

class CounterButton extends Component {

  //Deifne initial state in a constructor of the counter
  //
  constructor() {
    super();
    this.state = {
      counter: 0
    }
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
  }


  render() {

    return (

      <div className="counter" >
        <button onClick={this.increment}>+{this.props.by}</button>
        <button onClick={this.decrement}>-{this.props.by}</button>
        
      </div>
    )

  }

  increment() {
    this.setState(
      {
        counter: this.state.counter + this.props.by
      }
    );
    this.props.incrementMethod(this.props.by);
  }
  decrement() {
    this.setState(
      {
        counter: this.state.counter - this.props.by
      }
    );
    this.props.decrementMethod(this.props.by);
  }
}

CounterButton.defaultProps = {

  by: 0
}
CounterButton.protoTypes = {
  by: PropTypes.number
}
export default Counter;