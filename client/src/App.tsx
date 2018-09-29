import * as React from 'react';

interface IProps {
  test: string;
};

interface IState {
  data: any;
}

class App extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      data: []
    };
  }


  public render() {
    window.console.log('data:', this.state.data);
    return (
      <div className="App">
        <p>Hello world!</p>
      </div>
    );
  }
}

export default App;
