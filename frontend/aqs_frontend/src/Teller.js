// src/Teller.js
import React, { useState } from 'react';
import { Container, Row, Col, Card, CardBody, CardTitle, Button, Form, FormGroup, Label, Input } from 'reactstrap';
import './Teller.css';
import './customStyles.css'; // Import custom CSS

const transactionsForm1 = [
    'Cash Deposit', 'Cheque Deposit', 'Cheque Withdrawal', 'Cheque Deposit (FCY)', 'Cheque Withdrawal (FCY)'
];

const transactionsForm2 = [
    'Others', 'Imto', 'Fixed Deposit', 'Cash Withdrawal', 'Other Banks Cheque Deposit',
    'Funds Transfer', 'Cash Deposit (FCY)', 'Funds Transfer (FCY)', 'Managers Cheque Request',
    'Managers Cheque Liquidation', 'Fx Purchase'
];

const Teller = () => {
    const [showForm, setShowForm] = useState(false);
    const [selectedForm, setSelectedForm] = useState(null);

    const handleTransactionClick = (transaction) => {
        if (transactionsForm1.includes(transaction)) {
            setSelectedForm(1);
        } else {
            setSelectedForm(2);
        }
        setShowForm(true);
    };

    return (
        <Container>
            <h2 className="mt-4">Teller Transactions</h2>
            <Row>
                {[...transactionsForm1, ...transactionsForm2].map((transaction, index) => (
                    <Col key={index} md="6" className="mb-3">
                        <Card>
                            <CardBody>
                                <CardTitle tag="h5">{transaction}</CardTitle>
                                <Button onClick={() => handleTransactionClick(transaction)}>Select</Button>
                            </CardBody>
                        </Card>
                    </Col>
                ))}
            </Row>
            {showForm && (
                <div className="form-container">
                    <Card className="form-card">
                        <CardBody>
                            <Button color="link" onClick={() => setShowForm(false)}>← Back</Button>
                            <Form>
                                <FormGroup>
                                    <Label for="phoneNumber">Phone Number *</Label>
                                    <Input type="text" name="phone" id="phoneNumber" placeholder="Enter phone number" />
                                </FormGroup>
                                {selectedForm === 1 ? (
                                    <FormGroup>
                                        <Label for="transactionAccountNumber">Transaction Account Number *</Label>
                                        <Input type="text" name="transactionAccount" id="transactionAccountNumber" placeholder="Enter transaction account number" />
                                    </FormGroup>
                                ) : (
                                    <FormGroup>
                                        <Label for="accountNumber">Account Number *</Label>
                                        <Input type="text" name="account" id="accountNumber" placeholder="Enter account number" />
                                    </FormGroup>
                                )}
                                <Button color="primary" className="proceed-button">Proceed</Button>
                            </Form>
                        </CardBody>
                    </Card>
                </div>
            )}
        </Container>
    );
};

export default Teller;