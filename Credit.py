
VCE-2026-08-31-08-09-28.html

Page
1
/
1
100%
import 'package:flutter/material.dart';

void main() {
  runApp(const CreditGuardApp());
}

class CreditGuardApp extends StatelessWidget {
  const CreditGuardApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'CreditGuard',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF2563EB),
        ),
        scaffoldBackgroundColor: const Color(0xFFF5F7FB),
        fontFamily: 'Roboto',
      ),
      home: const HomeScreen(),
    );
  }
}

// ---------------------------------------------------------
// HOME SCREEN
// ---------------------------------------------------------

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Spacer(),

              Container(
                width: 72,
                height: 72,
                decoration: BoxDecoration(
                  color: const Color(0xFFE8F0FF),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: const Icon(
                  Icons.credit_score,
                  size: 40,
                  color: Color(0xFF2563EB),
                ),
              ),

              const SizedBox(height: 28),

              const Text(
                'CreditGuard',
                style: TextStyle(
                  fontSize: 38,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF111827),
                ),
              ),

              const SizedBox(height: 12),

              const Text(
                'Credit Card Default\nRisk Prediction',
                style: TextStyle(
                  fontSize: 25,
                  fontWeight: FontWeight.w600,
                  color: Color(0xFF374151),
                  height: 1.2,
                ),
              ),

              const SizedBox(height: 18),

              const Text(
                'Use machine learning to estimate the '
                'probability of credit card default.',
                style: TextStyle(
                  fontSize: 16,
                  color: Color(0xFF6B7280),
                  height: 1.5,
                ),
              ),

              const Spacer(),

              SizedBox(
                width: double.infinity,
                height: 56,
                child: ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            const CustomerDetailsScreen(),
                      ),
                    );
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF2563EB),
                    foregroundColor: Colors.white,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                  child: const Text(
                    'Start Prediction',
                    style: TextStyle(
                      fontSize: 17,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ),

              const SizedBox(height: 18),

              const Center(
                child: Text(
                  'ML-powered decision support tool',
                  style: TextStyle(
                    fontSize: 12,
                    color: Color(0xFF9CA3AF),
                  ),
                ),
              ),

              const SizedBox(height: 12),
            ],
          ),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------
// CUSTOMER DETAILS SCREEN
// ---------------------------------------------------------

class CustomerDetailsScreen extends StatefulWidget {
  const CustomerDetailsScreen({super.key});

  @override
  State<CustomerDetailsScreen> createState() =>
      _CustomerDetailsScreenState();
}

class _CustomerDetailsScreenState
    extends State<CustomerDetailsScreen> {

  final limitController = TextEditingController();
  final ageController = TextEditingController();

  int? education;
  int? marriage;
  int? sex;

  @override
  void dispose() {
    limitController.dispose();
    ageController.dispose();
    super.dispose();
  }

  void continueToRepayment() {

    if (limitController.text.isEmpty ||
        ageController.text.isEmpty ||
        education == null ||
        marriage == null ||
        sex == null) {

      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text(
            'Please complete all fields.',
          ),
        ),
      );

      return;
    }

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => RepaymentScreen(
          limitBalance:
              double.parse(limitController.text),
          age:
              int.parse(ageController.text),
          education:
              education!,
          marriage:
              marriage!,
          sex:
              sex!,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: const Text('Customer Details'),
      ),

      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),

        child: Column(
          crossAxisAlignment:
              CrossAxisAlignment.start,

          children: [

            const Text(
              'Basic Information',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 8),

            const Text(
              'Enter the customer information used '
              'by the prediction model.',
              style: TextStyle(
                color: Colors.grey,
              ),
            ),

            const SizedBox(height: 25),

            buildTextField(
              controller: limitController,
              label: 'Credit Limit',
              hint: 'Example: 200000',
              icon: Icons.account_balance_wallet,
              keyboardType:
                  TextInputType.number,
            ),

            const SizedBox(height: 16),

            buildTextField(
              controller: ageController,
              label: 'Age',
              hint: 'Example: 35',
              icon: Icons.person,
              keyboardType:
                  TextInputType.number,
            ),

            const SizedBox(height: 16),

            buildDropdown(
              label: 'Gender',
              value: sex,
              items: const {
                1: 'Male',
                2: 'Female',
              },
              onChanged: (value) {
                setState(() {
                  sex = value;
                });
              },
            ),

            const SizedBox(height: 16),

            buildDropdown(
              label: 'Education',
              value: education,
              items: const {
                1: 'Graduate School',
                2: 'University',
                3: 'High School',
                4: 'Others',
              },
              onChanged: (value) {
                setState(() {
                  education = value;
                });
              },
            ),

            const SizedBox(height: 16),

            buildDropdown(
              label: 'Marriage',
              value: marriage,
              items: const {
                1: 'Married',
                2: 'Single',
                3: 'Others',
              },
              onChanged: (value) {
                setState(() {
                  marriage = value;
                });
              },
            ),

            const SizedBox(height: 30),

            SizedBox(
              width: double.infinity,
              height: 54,

              child: ElevatedButton(
                onPressed: continueToRepayment,

                child: const Text(
                  'Continue',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget buildTextField({
    required TextEditingController controller,
    required String label,
    required String hint,
    required IconData icon,
    required TextInputType keyboardType,
  }) {

    return TextField(
      controller: controller,
      keyboardType: keyboardType,

      decoration: InputDecoration(
        labelText: label,
        hintText: hint,
        prefixIcon: Icon(icon),

        border: OutlineInputBorder(
          borderRadius:
              BorderRadius.circular(14),
        ),
      ),
    );
  }

  Widget buildDropdown({
    required String label,
    required int? value,
    required Map<int, String> items,
    required Function(int?) onChanged,
  }) {

    return DropdownButtonFormField<int>(
      value: value,

      decoration: InputDecoration(
        labelText: label,
        border: OutlineInputBorder(
          borderRadius:
              BorderRadius.circular(14),
        ),
      ),

      items: items.entries.map((entry) {

        return DropdownMenuItem<int>(
          value: entry.key,
          child: Text(entry.value),
        );

      }).toList(),

      onChanged: onChanged,
    );
  }
}

// ---------------------------------------------------------
// REPAYMENT SCREEN
// ---------------------------------------------------------

class RepaymentScreen extends StatefulWidget {

  final double limitBalance;
  final int age;
  final int education;
  final int marriage;
  final int sex;

  const RepaymentScreen({
    super.key,
    required this.limitBalance,
    required this.age,
    required this.education,
    required this.marriage,
    required this.sex,
  });

  @override
  State<RepaymentScreen> createState() =>
      _RepaymentScreenState();
}

class _RepaymentScreenState
    extends State<RepaymentScreen> {

  final pay0 = TextEditingController();
  final pay2 = TextEditingController();
  final pay3 = TextEditingController();
  final pay4 = TextEditingController();
  final pay5 = TextEditingController();
  final pay6 = TextEditingController();

  final bill0 = TextEditingController();
  final bill2 = TextEditingController();
  final bill3 = TextEditingController();
  final bill4 = TextEditingController();
  final bill5 = TextEditingController();
  final bill6 = TextEditingController();

  int? payStatus0;
  int? payStatus2;
  int? payStatus3;
  int? payStatus4;
  int? payStatus5;
  int? payStatus6;

  @override
  void dispose() {

    pay0.dispose();
    pay2.dispose();
    pay3.dispose();
    pay4.dispose();
    pay5.dispose();
    pay6.dispose();

    bill0.dispose();
    bill2.dispose();
    bill3.dispose();
    bill4.dispose();
    bill5.dispose();
    bill6.dispose();

    super.dispose();
  }

  void predict() {

    Navigator.push(
      context,

      MaterialPageRoute(
        builder: (context) => ResultScreen(
          prediction: 0,
          probability: 0.23,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(

      appBar: AppBar(
        title: const Text(
          'Financial Information',
        ),
      ),

      body: SingleChildScrollView(

        padding: const EdgeInsets.all(20),

        child: Column(

          crossAxisAlignment:
              CrossAxisAlignment.start,

          children: [

            const Text(
              'Payment History',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 8),

            const Text(
              'Enter the repayment information '
              'from the previous months.',
              style: TextStyle(
                color: Colors.grey,
              ),
            ),

            const SizedBox(height: 25),

            buildMonthSection(
              'September',
              pay0,
              bill0,
              payStatus0,
              (value) {
                setState(() {
                  payStatus0 = value;
                });
              },
            ),

            buildMonthSection(
              'August',
              pay2,
              bill2,
              payStatus2,
              (value) {
                setState(() {
                  payStatus2 = value;
                });
              },
            ),

            buildMonthSection(
              'July',
              pay3,
              bill3,
              payStatus3,
              (value) {
                setState(() {
                  payStatus3 = value;
                });
              },
            ),

            buildMonthSection(
              'June',
              pay4,
              bill4,
              payStatus4,
              (value) {
                setState(() {
                  payStatus4 = value;
                });
              },
            ),

            buildMonthSection(
              'May',
              pay5,
              bill5,
              payStatus5,
              (value) {
                setState(() {
                  payStatus5 = value;
                });
              },
            ),

            buildMonthSection(
              'April',
              pay6,
              bill6,
              payStatus6,
              (value) {
                setState(() {
                  payStatus6 = value;
                });
              },
            ),

            const SizedBox(height: 25),

            SizedBox(
              width: double.infinity,
              height: 56,

              child: ElevatedButton.icon(

                onPressed: predict,

                icon: const Icon(
                  Icons.analytics,
                ),

                label: const Text(
                  'Predict Default Risk',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ),

            const SizedBox(height: 30),
          ],
        ),
      ),
    );
  }

  Widget buildMonthSection(
    String month,
    TextEditingController payment,
    TextEditingController bill,
    int? status,
    Function(int?) onChanged,
  ) {

    return Card(

      margin: const EdgeInsets.only(
        bottom: 16,
      ),

      child: Padding(

        padding: const EdgeInsets.all(16),

        child: Column(

          crossAxisAlignment:
              CrossAxisAlignment.start,

          children: [

            Text(
              month,
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 14),

            TextField(
              controller: bill,
              keyboardType:
                  TextInputType.number,

              decoration: InputDecoration(
                labelText: 'Bill Amount',
                prefixIcon:
                    const Icon(Icons.receipt_long),

                border: OutlineInputBorder(
                  borderRadius:
                      BorderRadius.circular(12),
                ),
              ),
            ),

            const SizedBox(height: 12),

            TextField(
              controller: payment,
              keyboardType:
                  TextInputType.number,

              decoration: InputDecoration(
                labelText: 'Payment Amount',
                prefixIcon:
                    const Icon(Icons.payments),

                border: OutlineInputBorder(
                  borderRadius:
                      BorderRadius.circular(12),
                ),
              ),
            ),

            const SizedBox(height: 12),

            DropdownButtonFormField<int>(

              value: status,

              decoration: InputDecoration(
                labelText: 'Repayment Status',
                border: OutlineInputBorder(
                  borderRadius:
                      BorderRadius.circular(12),
                ),
              ),

              items: const [

                DropdownMenuItem(
                  value: -2,
                  child: Text(
                    'No consumption',
                  ),
                ),

                DropdownMenuItem(
                  value: -1,
                  child: Text(
                    'Paid duly',
                  ),
                ),

                DropdownMenuItem(
                  value: 0,
                  child: Text(
                    'Use of revolving credit',
                  ),
                ),

                DropdownMenuItem(
                  value: 1,
                  child: Text(
                    'Payment delay: 1 month',
                  ),
                ),

                DropdownMenuItem(
                  value: 2,
                  child: Text(
                    'Payment delay: 2 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 3,
                  child: Text(
                    'Payment delay: 3 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 4,
                  child: Text(
                    'Payment delay: 4 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 5,
                  child: Text(
                    'Payment delay: 5 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 6,
                  child: Text(
                    'Payment delay: 6 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 7,
                  child: Text(
                    'Payment delay: 7 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 8,
                  child: Text(
                    'Payment delay: 8 months',
                  ),
                ),

                DropdownMenuItem(
                  value: 9,
                  child: Text(
                    'Payment delay: 9+ months',
                  ),
                ),
              ],

              onChanged: onChanged,
            ),
          ],
        ),
      ),
    );
  }
}

// ---------------------------------------------------------
// RESULT SCREEN
// ---------------------------------------------------------

class ResultScreen extends StatelessWidget {

  final int prediction;
  final double probability;

  const ResultScreen({
    super.key,
    required this.prediction,
    required this.probability,
  });

  @override
  Widget build(BuildContext context) {

    final bool highRisk =
        prediction == 1;

    final percentage =
        (probability * 100).toStringAsFixed(1);

    return Scaffold(

      appBar: AppBar(
        title: const Text('Prediction Result'),
      ),

      body: Padding(

        padding: const EdgeInsets.all(24),

        child: Column(

          mainAxisAlignment:
              MainAxisAlignment.center,

          children: [

            Icon(
              highRisk
                  ? Icons.warning_amber_rounded
                  : Icons.check_circle_outline,

              size: 90,

              color: highRisk
                  ? Colors.red
                  : Colors.green,
            ),

            const SizedBox(height: 25),

            Text(
              highRisk
                  ? 'HIGH RISK'
                  : 'LOW RISK',

              style: TextStyle(
                fontSize: 32,
                fontWeight: FontWeight.bold,

                color: highRisk
                    ? Colors.red
                    : Colors.green,
              ),
            ),

            const SizedBox(height: 20),

            const Text(
              'Estimated Default Probability',
              style: TextStyle(
                fontSize: 16,
                color: Colors.grey,
              ),
            ),

            const SizedBox(height: 8),

            Text(
              '$percentage%',
              style: const TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 25),

            const Text(
              'This result is generated by a '
              'machine learning model and should '
              'not be treated as a financial decision.',
              textAlign: TextAlign.center,

              style: TextStyle(
                color: Colors.grey,
                height: 1.5,
              ),
            ),

            const SizedBox(height: 35),

            SizedBox(
              width: double.infinity,
              height: 52,

              child: ElevatedButton(

                onPressed: () {

                  Navigator.popUntil(
                    context,
                    (route) => route.isFirst,
                  );

                },

                child: const Text(
                  'New Prediction',
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
Displaying VCE-2026-08-31-08-09-28.html.