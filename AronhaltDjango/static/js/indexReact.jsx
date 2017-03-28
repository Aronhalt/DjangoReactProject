var ProjectComponent = React.createClass({
	render: function(){
		var teststyle ={fontSize: '18px', marginRight: '20px'};
		return(
				<div style={testStyle}>
					is this text is 18px tall?
				</div>
		}
	}
});

React.render(
	<ProjectComponent />,
	document.getElementById('content')
	)
