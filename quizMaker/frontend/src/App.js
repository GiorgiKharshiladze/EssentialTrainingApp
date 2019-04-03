import React, { Component } from 'react';
import './Styles/App.css';
import "./Styles/quizMaker.css";
import AutosizeInput from 'react-input-autosize';

class App extends Component {
  constructor(props) {
    super(props);
    // Don't call this.setState() here!
    this.state = {
      counter: "sfs", test: "",
      object: <input></input>,
      inputs: ['input-0'],
      text: '',
      newText: "",
      refresh: false,
      variableNumber: 0,
      outputArray: '',
      outputs: [""],
      selectedOutput: 0,
    };

    this.x = [];
    // this.addTag = this.addTag.bind(this);
    this.appendToArray = this.appendToArray.bind(this);
  }



  appendToArray(ex) {
    var newInput = 'input-${this.state.inputs.length}';
    this.setState({ newText: this.state.newText + this.state.text })
    this.state.inputs[0] = "fqwe"
    console.log(this.state.inputs)


    switch (ex) {
      case "string":
        this.setState({ inputs: this.state.inputs.concat(["string"]) });
        break;
      case "sqrt":
        this.setState({ variableNumber: this.state.variableNumber + 1, inputs: this.state.inputs.concat(["a" + this.state.variableNumber.toString(), "string"]) });
        break;
      default:
        this.setState({ inputs: this.state.inputs.concat([]) });
        break;
    }
    //console.log(this.state.newText)
  }


  onChangeAge() {
    this.setState({ refresh: !this.state.refresh })
  }


  render() {
    return (
      <div style={{ backgroundColor: "#F3F6F8", width: "100%",  height:2000 }}>
        <div id='mainContainer'>
          <div>
          <div id="QuizMakerTitle" >QuizMaker</div>

          <div style={{ display: 'flex', flexDirection: 'row' }}>
            <div>
              <div id="canvas">
                {this.state.inputs.map((item, index) => {
                  //console.log("The current iteration is: " + index);
                  if (item[0] == "a") {
                    return (<input id="variables" value={item} onChange={this.onChangeAge.bind(this)} />)
                  }
                  else {
                    return (<input  
                      onChange={(e) => {
                        this.x = this.state.inputs;
                        this.x[index] = e.target.value;
                        console.log("=====")
                        console.log(this.x)
                        console.log("=====")
                        this.setState({refresh:!this.state.refresh})
                        // this.onChangeAge();
                      }
                    
                      }
                      
                      style={{backgroundColor:'#E8E9EA', padding:9, borderWidth:0, borderRadius:10, width:this.state.inputs[index].length*6.5 }}
                       value={this.state.inputs[index]}

                    />)
                  }   
                  }
              
                )}
              </div>
            </div>

            <div style={{ marginLeft: 30 }}>
              <div style={{ display: 'flex', flexDirection: 'column' }}>
                <button id="addVariable" onClick={() => this.appendToArray("sqrt")}> Add Variable </button>

                <div id="mathTitle"> Math Functions </div>
                <div style={{ width: 400, flexWrap: 'wrap' }}>
                  <button id="mathButtons" onClick={() => this.setState({ outputArray: this.state.outputArray + 'Math.sqrt' })}> sqrt </button>
                  <button id="mathButtons" onClick={() => {this.state.outputs[this.state.selectedOutput] = this.state.outputs[this.state.selectedOutput] + '+' ; this.setState({refresh:!this.state.refresh}) }}> add </button>
                  <button id="mathButtons" onClick={() => this.appendToArray("sqrt")}> sub </button>
                  <button id="mathButtons" onClick={() => this.appendToArray("sqrt")}> div </button>
                  <button id="mathButtons" onClick={() => this.appendToArray("sqrt")}> mul </button>
                  <button id="mathButtons" onClick={() => this.appendToArray("sqrt")}> mod </button>
                  <button id="mathButtons" onClick={() => console.log(this.x)}> array output </button>

                </div>
              </div>
            </div>
          </div>


          <div>
            {this.state.inputs.map((item, index) => {
              //console.log("The current iteration is: " + index);
              if (item[0] == "a") {
                return (<button id="outputVariables"  
                  onClick={() => { this.state.outputs[this.state.selectedOutput] = this.state.outputs[this.state.selectedOutput] + item; this.setState({ refresh: !this.state.refresh }) }}
                  onChange={this.onChangeAge.bind(this)}>
                  {item}
                </button>
                )
              }

            }
            )}

          </div>

          <div>
            <div id="outputTitle">Ouput</div>
            <div style={{ flexDirection: 'row', display: 'flex' }}>
              <div>
                {/* Ouputs */}
                {this.state.outputs.map((item, index) => {
                  //console.log("The current iteration is: " + index);
                  return (
                  <div style={{flexDirection:'column', marginBottom:15,}}>
                  <input id="outputCanvas" onClick={() => this.setState({ selectedOutput: index })} value={this.state.outputs[index]}  />
                  </div>
                  )})}
              </div>
              <div onClick={() => this.setState({ outputs: this.state.outputs.concat([""]) })} id="addOutput" >Add output</div>
            </div>
          </div>


          </div>

        </div>
      </div>
    );
  }
}

export default App;
