import axios from 'axios';
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

  public componentDidMount() {
    axios.get('http://localhost:5000/items', {
      headers: {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzcyNDYxMDEsImlhdCI6MTUzNzI0NTgwMSwibmJmIjoxNTM3MjQ1ODAxLCJpZGVudGl0eSI6MX0.RnG05g17_tn0pQIit30a9yqORjPPm6hPmuasnuPo0EM',
      }
    })
      .then(res => {
        window.console.log(res);
        this.setState({ data: res.data.items });
      })
      .catch(err => {
        window.console.log('err:', err);
      })
  };

  public render() {
    window.console.log('data:', this.state.data);
    return (
      <div className="App">
        { this.state.data.map((key: any) => {
          return key.name
        })}
      </div>
    );
  }
}

export default App;
