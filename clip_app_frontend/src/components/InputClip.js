import React from 'react';
import { Button } from 'semantic-ui-react';
import styled from 'styled-components';

const HeadBlock = styled.div`
  padding-top: 48px;
  padding-left: 32px;
  padding-right: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid #e9ecef;
  h1 {
    margin: 0;
    font-size: 36px;
    color: #343a40;
  }
  .tasks-left {
    color: #20c997;
    font-size: 18px;
    margin-top: 40px;
    font-weight: bold;
    float: left;
  }
  .tasks-right {
    color: #20c997;
    font-size: 18px;
    margin-top: 40px;
    font-weight: bold;
    float: right;
  }
`;

function InputClip() {
  return (
    <HeadBlock>
        HELLO
        <div className="tasks-left">
            <Button content='Choose File' labelPosition='left' icon='file' />
            <Button content='Upload' labelPosition='left' icon='cloud upload' />
        </div>
        <div className="tasks-right">
            texts <br />
            texts
        </div>
    </HeadBlock>
  );
}


export default InputClip;